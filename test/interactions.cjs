const vm = require('node:vm');
const fs = require('node:fs');
const assert = require('node:assert/strict');
for (const blocked of [false,true]) {
 const listeners={};
 const elements={language:{textContent:'EN',setAttribute(k,v){this[k]=v},addEventListener(k,v){listeners.language=v}},theme:{setAttribute(k,v){this[k]=v},addEventListener(k,v){listeners.theme=v}}};
 const translated={dataset:{zh:'中文内容',en:'English content'},textContent:'中文内容'};
 const root={dataset:{theme:'light'},lang:'zh-CN'};
 const context={document:{documentElement:root,getElementById:id=>elements[id],querySelectorAll:()=>[translated]},localStorage:{getItem(){if(blocked)throw Error('blocked');return 'dark'},setItem(){if(blocked)throw Error('blocked')}}};
 vm.runInNewContext(fs.readFileSync(require('node:path').join(__dirname,'../src/site.js'),'utf8'),context);
 assert.equal(root.dataset.theme,blocked?'light':'dark');
 listeners.language();assert.equal(root.lang,'en');assert.equal(translated.textContent,'English content');
 listeners.theme();assert.equal(root.dataset.theme,blocked?'dark':'light');assert.match(elements.theme['aria-label'],/Switch to/);
 listeners.language();assert.equal(root.lang,'zh-CN');assert.equal(translated.textContent,'中文内容');
}
console.log('PASS: language/theme interactions, saved theme, blocked storage, accessible labels');
