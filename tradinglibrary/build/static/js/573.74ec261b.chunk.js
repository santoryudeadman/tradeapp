/*! For license information please see 573.74ec261b.chunk.js.LICENSE.txt */
"use strict";(self.webpackChunktradinglibrary=self.webpackChunktradinglibrary||[]).push([[573],{573:(e,t,i)=>{i.r(t),i.d(t,{KEYBOARD_DID_CLOSE:()=>o,KEYBOARD_DID_OPEN:()=>s,copyVisualViewport:()=>D,keyboardDidClose:()=>w,keyboardDidOpen:()=>c,keyboardDidResize:()=>l,resetKeyboardAssist:()=>n,setKeyboardClose:()=>g,setKeyboardOpen:()=>b,startKeyboardAssist:()=>h,trackViewportChanges:()=>u});const s="ionKeyboardDidShow",o="ionKeyboardDidHide";let a={},r={},d=!1;const n=()=>{a={},r={},d=!1},h=e=>{p(e),e.visualViewport&&(r=D(e.visualViewport),e.visualViewport.onresize=()=>{u(e),c()||l(e)?b(e):w(e)&&g(e)})},p=e=>{e.addEventListener("keyboardDidShow",(t=>b(e,t))),e.addEventListener("keyboardDidHide",(()=>g(e)))},b=(e,t)=>{y(e,t),d=!0},g=e=>{f(e),d=!1},c=()=>{const e=(a.height-r.height)*r.scale;return!d&&a.width===r.width&&e>150},l=e=>d&&!w(e),w=e=>d&&r.height===e.innerHeight,y=(e,t)=>{const i=t?t.keyboardHeight:e.innerHeight-r.height,o=new CustomEvent(s,{detail:{keyboardHeight:i}});e.dispatchEvent(o)},f=e=>{const t=new CustomEvent(o);e.dispatchEvent(t)},u=e=>{a=Object.assign({},r),r=D(e.visualViewport)},D=e=>({width:Math.round(e.width),height:Math.round(e.height),offsetTop:e.offsetTop,offsetLeft:e.offsetLeft,pageTop:e.pageTop,pageLeft:e.pageLeft,scale:e.scale})}}]);
//# sourceMappingURL=573.74ec261b.chunk.js.map