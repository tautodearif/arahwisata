/* Fonctions pures, réutilisables pour vérification sans navigateur. */
(function(root){
 const methods={
  quote(program,count){if(!program||!Number.isInteger(count)||count<1||count>100)throw new Error('Jumlah peserta harus 1–100.');const groups=Math.ceil(count/program.capacity);return {groups,total:groups*program.capacity*program.price,deposit:groups*program.capacity*program.price*.5};},
  escape(value){return String(value??'').replace(/[&<>"']/g,c=>({'&':'&amp;','<':'&lt;','>':'&gt;','"':'&quot;',"'":'&#39;'}[c]));},
  money(value){return new Intl.NumberFormat('id-ID',{style:'currency',currency:'IDR',maximumFractionDigits:0}).format(value);},
  csv(rows){return '\uFEFF'+rows.map(row=>row.map(v=>{let s=String(v??'');if(/^[=+\-@\t\r]/.test(s))s="'"+s;return '"'+s.replace(/"/g,'""')+'"';}).join(',')).join('\r\n');},
  validRecord(r){return r&&typeof r.id==='string'&&r.id.length<100&&['transaksi','stok','kapasitas','dampak'].includes(r.type)&&typeof r.label==='string'&&r.label.length<=150&&typeof r.category==='string'&&r.category.length<=150&&typeof r.notes==='string'&&r.notes.length<=2000&&/^\d{4}-\d{2}-\d{2}$/.test(r.date)&&Number.isFinite(r.value)&&r.value>=0&&r.value<=1e11&&['green','yellow','red'].includes(r.status);}
 };if(typeof module!=='undefined'&&module.exports)module.exports=methods;else root.ArahCore=methods;
})(typeof window!=='undefined'?window:globalThis);
