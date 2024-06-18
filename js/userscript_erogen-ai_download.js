// ==UserScript==
// @name        Download from erogen.ai
// @match       https://erogen.ai/*
// @grant       GM_setValue
// @grant       GM_getValue
// @version     1.0
// @author      saperoi @ icosahedr.online
// @description Download character JSONs from Erogen.AI, as the original API JSON, or converted to the Character Card V2 format.
// ==/UserScript==

var charId = window.location.pathname.split('/')[1];
var apiURL = "https://api.erogen.ai/";
var cloudfrontURL = "https://d1jair33c02u34.cloudfront.net/";

function cookieMonster() {
    var cookie = GM_getValue("erogenAICookie", "");
    if (cookie == "") { cookie = prompt("corinth-app/session=???", "Cookie Value Here"); GM_setValue("erogenAICookie", cookie); }
    return cookie;
}

async function downloadCard() {
    cookie = cookieMonster();
    const response = await fetch("https://api.erogen.ai/characters/" + charId, {
        "credentials": "include",
        "headers": {
        "Cookie": cookie
        },
        "method": "GET",
        "mode": "cors"
    });
    const charData = await response.json();
    console.log(charData);
    return charData;
}

function convertCard(charData) {
    function removeTag(text) {
        var corr = {"<p>": "", "</p>": `\n`, "<em>": "*", "</em>": "*"}
        for (const c in corr) { text = text.replaceAll(c, corr[c]); }
        return text.trim();
    }

    result = Object();
    data = Object();

    data.alternate_greetings = [];
    if (charData.avatarKey == null) { data.avatar = cloudfrontURL + charData.avatars[0].key; } else { data.avatar = cloudfrontURL + charData.avatarKey; }
    data.character_book = null;
    data.character_version = charData.version;
    data.creator = charData.creatorId;
    data.creator_notes = charData.creatorNotes;

    data.description = removeTag(charData.description) + `\n\n` +  removeTag(charData.appearance);
    data.first_mes = removeTag(charData.firstMessage);
    data.mes_example = removeTag(charData.messageExamples);
    data.name = charData.givenName;
    data.personality = removeTag(charData.personality);
    data.post_history_instructions = "";
    data.scenario = removeTag(charData.scenario);
    data.system_prompt = "";
    data.tags = [];
    for (const c of charData.characterTags) { data.tags = data.tags.concat(c.tag.standardDisplayName)}
    for (const c of charData.characterCategories) { data.tags = data.tags.concat(c.category.displayName)}

    result.data = data;
    result.spec = "chara_card_v2";
    result.spec_version = "2.0";
    return result;
}

function showCard(result) {
    var dataStr = "data:application/json;charset=utf-8," + encodeURIComponent(JSON.stringify(result));
    window.open(dataStr, '_blank').focus();
}

cookieMonster();

function makeButtons() {
    api = document.createElement('button');
    api.className = "flex items-center justify-center text-left whitespace-nowrap select-none transition-all py-1.5 px-2.5 text-xs font-medium rounded-[5px] dark:bg-neutral-800 dark:text-neutral-400 dark:hover:bg-[#1C1C1C] h-7";
    api.innerHTML = '<a>API</a>';
    api.addEventListener("click", async (e) => { showCard(await downloadCard()); });

    dl = document.createElement('button');
    dl.className = "flex items-center justify-center text-left whitespace-nowrap select-none transition-all py-1.5 px-2.5 text-xs font-medium rounded-[5px] dark:bg-neutral-800 dark:text-neutral-400 dark:hover:bg-[#1C1C1C] h-7";
    dl.innerHTML = '<a>DL</a>';
    dl.addEventListener("click", async (e) => { showCard(convertCard(await downloadCard())); });

    window.addEventListener("load", function() {
        console.log(window.location.pathname.split('/')[2]);
        if ([undefined, "avatars", "chat", "system", "my-interactions"].includes(window.location.pathname.split('/')[2])) { selector = "div.space-x-3:nth-child(2)" }
        if (["chats"].includes(window.location.pathname.split('/')[2])) { selector = ".grid" }

        (new MutationObserver(check)).observe(document, {childList: true, subtree: true});
        function check(changes, observer) {
            if(document.querySelector(selector)) {
                observer.disconnect();
                if (!document.querySelector(selector).outerHTML.includes(api.outerHTML) || !document.querySelector(selector).outerHTML.includes(dl.outerHTML)) {
                    document.querySelector(selector).appendChild(api);
                    document.querySelector(selector).appendChild(dl);
                }
            }
        }
    });
}

makeButtons();

document.addEventListener("click", function(){
    makeButtons();
});