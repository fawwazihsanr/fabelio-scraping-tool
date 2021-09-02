(this["webpackJsonpfabelio-frontend"]=this["webpackJsonpfabelio-frontend"]||[]).push([[0],{37:function(t,e,n){},38:function(t,e,n){},58:function(t,e,n){},59:function(t,e,n){},65:function(t,e,n){"use strict";n.r(e);var c=n(1),a=n.n(c),i=n(27),s=n.n(i),r=(n(37),n.p,n(38),n(28)),o=n(2),j=n(8),l=n(9),d=n(11),h=n(10),u=n(32),b=n(31),O=n(16),p=n.n(O),f=p.a.create({baseURL:"http://localhost:8004",headers:{"Content-Type":"application/json",accept:"application/json"},transformRequest:[function(t,e){return t&&t.data?Object(u.a)({},t.data):t}].concat(Object(b.a)(p.a.defaults.transformRequest))}),x=n(0),m=function(t){Object(d.a)(n,t);var e=Object(h.a)(n);function n(t){var c;return Object(j.a)(this,n),(c=e.call(this,t)).handleChange=function(t){var e=c.state.fields,n=t.target,a=n.id,i=n.value;e[a]=i,c.setState({fields:e})},c.submitUrl=function(){(function(t){return f.post("submission",t)})({url:c.state.fields.url}).then((function(t){c.props.history.push("/detail/".concat(t.data.id))})).catch((function(t){alert("error")}))},c.state={fields:{}},c}return Object(l.a)(n,[{key:"render",value:function(){return Object(x.jsxs)("div",{className:"create-container",children:[Object(x.jsx)("h2",{children:"Input fabelio product url:"}),Object(x.jsxs)("div",{className:"wrapper-input",style:{display:"flex"},children:[Object(x.jsx)("input",{id:"url",type:"text",onChange:this.handleChange,value:this.state.fields.url}),Object(x.jsx)("button",{onClick:this.submitUrl,children:"submit"})]})]})}}]),n}(a.a.Component),v=(n(58),function(t){Object(d.a)(n,t);var e=Object(h.a)(n);function n(t){var c;return Object(j.a)(this,n),(c=e.call(this,t)).state={product:[]},c}return Object(l.a)(n,[{key:"componentDidMount",value:function(){var t=this;f.get("submission/list").then((function(e){t.setState({product:e.data})})).catch((function(t){alert("something error")}))}},{key:"render",value:function(){return Object(x.jsx)("div",{className:"list-container",children:Object(x.jsxs)("table",{children:[Object(x.jsxs)("tr",{children:[Object(x.jsx)("th",{children:"name"}),Object(x.jsx)("th",{children:"description"}),Object(x.jsx)("th",{children:"price"}),Object(x.jsx)("th",{children:"link"})]}),this.state.product.length>0?this.state.product.map((function(t,e){return Object(x.jsxs)("tr",{children:[Object(x.jsx)("td",{children:t.name}),Object(x.jsx)("td",{children:t.description}),Object(x.jsx)("td",{children:t.price}),Object(x.jsx)("a",{href:"/detail/".concat(t.id),children:Object(x.jsx)("td",{children:"".concat(window.location.hostname,"/detail/").concat(t.id)})})]})})):Object(x.jsx)(x.Fragment,{})]})})}}]),n}(a.a.Component)),g=(n(59),function(t){Object(d.a)(n,t);var e=Object(h.a)(n);function n(t){var c;return Object(j.a)(this,n),(c=e.call(this,t)).state={data:{}},c}return Object(l.a)(n,[{key:"componentDidMount",value:function(){var t,e=this;(t=this.props.match.params.id,f.get("submission/".concat(t))).then((function(t){e.setState({data:t.data})}))}},{key:"render",value:function(){var t=this.state.data;return Object(x.jsxs)("div",{className:"detail-container",children:[Object(x.jsxs)("table",{children:[Object(x.jsxs)("tr",{children:[Object(x.jsx)("th",{children:"name"}),Object(x.jsx)("th",{children:"description"}),Object(x.jsx)("th",{children:"price"})]}),Object(x.jsxs)("tr",{children:[Object(x.jsx)("td",{children:t.name}),Object(x.jsx)("td",{children:t.description}),Object(x.jsx)("td",{children:t.price})]})]}),Object(x.jsx)("span",{children:"Image"}),Object(x.jsx)("img",{src:t.image})]})}}]),n}(a.a.Component)),y=function(t){Object(d.a)(n,t);var e=Object(h.a)(n);function n(t){return Object(j.a)(this,n),e.call(this,t)}return Object(l.a)(n,[{key:"render",value:function(){return Object(x.jsxs)("div",{className:"home",style:{display:"flex",marginBottom:"20px",gap:"10px"},children:[Object(x.jsxs)("a",{href:"/",children:[" ",Object(x.jsx)("span",{children:"Create"})]}),Object(x.jsx)("a",{href:"/list",children:Object(x.jsx)("span",{children:"List"})})]})}}]),n}(a.a.Component);var C=function(){return Object(x.jsx)(r.a,{children:Object(x.jsxs)("div",{className:"App",children:[Object(x.jsx)(y,{}),Object(x.jsxs)(o.c,{children:[Object(x.jsx)(o.a,{exact:!0,path:"/",component:m}),Object(x.jsx)(o.a,{path:"/list",component:v}),Object(x.jsx)(o.a,{path:"/detail/:id",component:g})]})]})})},k=function(t){t&&t instanceof Function&&n.e(3).then(n.bind(null,66)).then((function(e){var n=e.getCLS,c=e.getFID,a=e.getFCP,i=e.getLCP,s=e.getTTFB;n(t),c(t),a(t),i(t),s(t)}))};s.a.render(Object(x.jsx)(a.a.StrictMode,{children:Object(x.jsx)(C,{})}),document.getElementById("root")),k()}},[[65,1,2]]]);
//# sourceMappingURL=main.7e8eb89d.chunk.js.map