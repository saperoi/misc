// ==UserScript==
// @name        muah.ai card download
// @match       *://card.muah.ai/*/
// @grant       none
// @version     1.0
// @author      saperoi @ icosahedr.online
// @description 8/6/2024, 22:23:57
// ==/UserScript==

sect = document.getElementsByClassName("download-button")[0];
sect.innerHTML = sect.innerHTML.replace("Import Now", "Download Now").replace("https://muah.ai/card?url=", "");