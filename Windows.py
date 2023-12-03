
// ==UserScript==
// @name         Fluxus Key System Bypasser v2
// @version      2.4
// @description  Bypass the Fluxus Key System with ease! Now gets a key in less than a few seconds! Thank you to Portal (woah24 on Discord) for the way better formatted and simplified code!
// @author       TheCtkHoster / Portal
// @match        *://linkvertise.com/*
// @match        *://*.flux.li/*
// @match        *://*.fluxteam.net/*
// @grant        none
// @icon         https://www.google.com/s2/favicons?domain=fluxteam.net
// @license      MIT
// @namespace https://greasyfork.org/users/1160145
// ==/UserScript==
 
(function() {
    'use strict';
 
    const redirectMap = {
        "https://linkvertise.com/152666/fluxus-windows-check-1/1": "fluxteam.net/windows/checkpoint/check1.php",
        "https://linkvertise.com/152666/fluxus-windows-check-2/1": "fluxteam.net/windows/checkpoint/check2.php",
        "https://linkvertise.com/152666/fluxus-windows-main/1": "fluxteam.net/windows/checkpoint/main.php",
        "https://fluxteam.net/windows/checkpoint/check1.php": "linkvertise.com/152666/fluxus-windows-check-2/1",
        "https://fluxteam.net/windows/checkpoint/check2.php": "linkvertise.com/152666/fluxus-windows-main/1",
    };
 
    const currentURL = window.location.href;
 
    if (currentURL in redirectMap) {
        window.location.replace(`https://${redirectMap[currentURL]}`);
    }
 
    if(currentURL === "https://fluxteam.net/windows/checkpoint/check1.php") {
 
    localStorage.setItem('startTime', Date.now()); //Ty Portal (woah24 on Discord) for this!
 
    }
 
    if (location.href.includes(".nexus" && "start.php")) {
        showNotification( { r: 0, g: 128, b: 0 }, "Please wait for Nexus verification...");
    }
 
 
    if (currentURL.includes("flux.li/windows/start.php?HWID=")) {
        const HWID = currentURL.split("=")[1];
        showNotification( { r: 0, g: 128, b: 0 }, "Got HWID! Completing Key System...");
        window.location.href = `https://flux.li/windows/start.php?7b20bcc1dfe26db966bb84f159da392f=false&HWID=${HWID}`;
    }
 
    if (currentURL === "https://flux.li/windows/start.php") {
        showNotification( { r: 255, g: 0, b: 0 }, "No HWID has been entered into the URL! Please enter your HWID into the URL and try again.");
    }
 
    if (currentURL === "https://fluxteam.net/windows/checkpoint/main.php") {
        window.stop();
        const startTime = localStorage.getItem('startTime');
        if (startTime) {
        const endTime = Date.now();
        const elapsedSeconds = Math.floor((endTime - parseInt(startTime)) / 1000);
        showNotification(
        { r: 0, g: 128, b: 0 },
        `Successfully bypassed Fluxus Keysystem! It took ${elapsedSeconds} seconds to reach here. Please copy your key and paste it into Fluxus.`
      );
      localStorage.removeItem('startTime')
   } else {
      showNotification(
        { r: 0, g: 128, b: 0 },
        'Successfully bypassed Fluxus Keysystem!'
      );
    }
}
 
  function showNotification(color, message) {
    const notificationDiv = document.createElement('div');
    notificationDiv.style.backgroundColor = `rgb(${color.r}, ${color.g}, ${color.b})`;
    notificationDiv.style.color = 'white';
    notificationDiv.style.position = 'fixed';
    notificationDiv.style.top = '0';
    notificationDiv.style.left = '0';
    notificationDiv.style.width = '100%';
    notificationDiv.style.padding = '10px';
    notificationDiv.style.textAlign = 'center';
    notificationDiv.style.fontWeight = 'bold';
    notificationDiv.textContent = message;
    document.body.appendChild(notificationDiv);
    setTimeout(() => {
      document.body.removeChild(notificationDiv);
    }, 4000); //Ty Portal (woah24 on Discord) for the simplified code :)
  }
})();
