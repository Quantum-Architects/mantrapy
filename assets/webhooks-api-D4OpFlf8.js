import{u as r,j as e}from"./index-BHCmrC2Q.js";const d={title:"Mantrapy Webhook API Documentation",description:"undefined"};function i(n){const s={a:"a",code:"code",div:"div",h1:"h1",h2:"h2",h3:"h3",header:"header",li:"li",p:"p",pre:"pre",span:"span",strong:"strong",ul:"ul",...r(),...n.components};return e.jsxs(e.Fragment,{children:[e.jsx(s.header,{children:e.jsxs(s.h1,{id:"mantrapy-webhook-api-documentation",children:["Mantrapy Webhook API Documentation",e.jsx(s.a,{"aria-hidden":"true",tabIndex:"-1",href:"#mantrapy-webhook-api-documentation",children:e.jsx(s.div,{"data-autolink-icon":!0})})]})}),`
`,e.jsx(s.p,{children:"This API allows clients to register, manage, and retrieve webhooks that listen for specific events on the Mantra blockchain. The API processes blockchain events in real-time and notifies registered webhooks based on customizable query conditions."}),`
`,e.jsxs(s.h2,{id:"table-of-contents",children:["Table of Contents",e.jsx(s.a,{"aria-hidden":"true",tabIndex:"-1",href:"#table-of-contents",children:e.jsx(s.div,{"data-autolink-icon":!0})})]}),`
`,e.jsxs(s.ul,{children:[`
`,e.jsx(s.li,{children:e.jsx(s.a,{href:"#installation",children:"Installation"})}),`
`,e.jsx(s.li,{children:e.jsx(s.a,{href:"#usage",children:"Usage"})}),`
`,e.jsxs(s.li,{children:[e.jsx(s.a,{href:"#endpoints",children:"Endpoints"}),`
`,e.jsxs(s.ul,{children:[`
`,e.jsx(s.li,{children:e.jsx(s.a,{href:"#post-webhooks",children:e.jsx(s.code,{children:"POST /webhooks/"})})}),`
`,e.jsx(s.li,{children:e.jsx(s.a,{href:"#delete-webhooksid",children:e.jsx(s.code,{children:"DELETE /webhooks/{hook_id}"})})}),`
`,e.jsx(s.li,{children:e.jsx(s.a,{href:"#get-webhooks",children:e.jsx(s.code,{children:"GET /webhooks/"})})}),`
`,e.jsx(s.li,{children:e.jsx(s.a,{href:"#get-webhooksid",children:e.jsx(s.code,{children:"GET /webhooks/{hook_id}"})})}),`
`]}),`
`]}),`
`,e.jsx(s.li,{children:e.jsx(s.a,{href:"#event-query-format",children:"Event Query Format"})}),`
`,e.jsx(s.li,{children:e.jsx(s.a,{href:"#error-handling",children:"Error Handling"})}),`
`]}),`
`,e.jsxs(s.h2,{id:"installation",children:["Installation",e.jsx(s.a,{"aria-hidden":"true",tabIndex:"-1",href:"#installation",children:e.jsx(s.div,{"data-autolink-icon":!0})})]}),`
`,e.jsxs(s.p,{children:["Ensure you have ",e.jsx(s.code,{children:"FastAPI"}),", ",e.jsx(s.code,{children:"asyncio"}),", and the necessary database dependencies installed in your environment."]}),`
`,e.jsx(s.pre,{className:"shiki shiki-themes github-light github-dark-dimmed",style:{backgroundColor:"#fff","--shiki-dark-bg":"#22272e",color:"#24292e","--shiki-dark":"#adbac7"},tabIndex:"0",children:e.jsx(s.code,{children:e.jsxs(s.span,{className:"line",children:[e.jsx(s.span,{style:{color:"#6F42C1","--shiki-dark":"#F69D50"},children:"pip"}),e.jsx(s.span,{style:{color:"#032F62","--shiki-dark":"#96D0FF"},children:" install"}),e.jsx(s.span,{style:{color:"#032F62","--shiki-dark":"#96D0FF"},children:" fastapi"}),e.jsx(s.span,{style:{color:"#032F62","--shiki-dark":"#96D0FF"},children:" uvicorn"}),e.jsx(s.span,{style:{color:"#032F62","--shiki-dark":"#96D0FF"},children:" sqlalchemy"})]})})}),`
`,e.jsxs(s.h2,{id:"usage",children:["Usage",e.jsx(s.a,{"aria-hidden":"true",tabIndex:"-1",href:"#usage",children:e.jsx(s.div,{"data-autolink-icon":!0})})]}),`
`,e.jsx(s.p,{children:"Run the FastAPI application with:"}),`
`,e.jsx(s.pre,{className:"shiki shiki-themes github-light github-dark-dimmed",style:{backgroundColor:"#fff","--shiki-dark-bg":"#22272e",color:"#24292e","--shiki-dark":"#adbac7"},tabIndex:"0",children:e.jsx(s.code,{children:e.jsxs(s.span,{className:"line",children:[e.jsx(s.span,{style:{color:"#6F42C1","--shiki-dark":"#F69D50"},children:"uvicorn"}),e.jsx(s.span,{style:{color:"#032F62","--shiki-dark":"#96D0FF"},children:" your_module_name:app"}),e.jsx(s.span,{style:{color:"#005CC5","--shiki-dark":"#6CB6FF"},children:" --reload"})]})})}),`
`,e.jsxs(s.p,{children:["Replace ",e.jsx(s.code,{children:"your_module_name"})," with the name of the file where the FastAPI ",e.jsx(s.code,{children:"app"})," is defined."]}),`
`,e.jsxs(s.h2,{id:"endpoints",children:["Endpoints",e.jsx(s.a,{"aria-hidden":"true",tabIndex:"-1",href:"#endpoints",children:e.jsx(s.div,{"data-autolink-icon":!0})})]}),`
`,e.jsxs(s.h3,{id:"post-webhooks",children:["POST ",e.jsx(s.code,{children:"/webhooks/"}),e.jsx(s.a,{"aria-hidden":"true",tabIndex:"-1",href:"#post-webhooks",children:e.jsx(s.div,{"data-autolink-icon":!0})})]}),`
`,e.jsx(s.p,{children:"Creates a new webhook that listens to specific blockchain events."}),`
`,e.jsx(s.strong,{children:"Request Body"}),`
`,e.jsxs(s.ul,{children:[`
`,e.jsxs(s.li,{children:[e.jsx(s.code,{children:"url"})," (str): The webhook endpoint URL."]}),`
`,e.jsxs(s.li,{children:[e.jsx(s.code,{children:"query"})," (str): Conditions to filter blockchain events. Example: ",e.jsx(s.code,{children:'"module=bank&value=/cosmos.bank.v1beta1.MsgSend  "'})]}),`
`]}),`
`,e.jsx(s.strong,{children:"Response"}),`
`,e.jsxs(s.ul,{children:[`
`,e.jsxs(s.li,{children:[e.jsx(s.strong,{children:"200 Created"}),": Webhook created successfully."]}),`
`]}),`
`,e.jsx(s.pre,{className:"shiki shiki-themes github-light github-dark-dimmed",style:{backgroundColor:"#fff","--shiki-dark-bg":"#22272e",color:"#24292e","--shiki-dark":"#adbac7"},tabIndex:"0",children:e.jsxs(s.code,{children:[e.jsx(s.span,{className:"line",children:e.jsx(s.span,{style:{color:"#24292E","--shiki-dark":"#ADBAC7"},children:"{"})}),`
`,e.jsxs(s.span,{className:"line",children:[e.jsx(s.span,{style:{color:"#005CC5","--shiki-dark":"#8DDB8C"},children:'  "message"'}),e.jsx(s.span,{style:{color:"#24292E","--shiki-dark":"#ADBAC7"},children:": "}),e.jsx(s.span,{style:{color:"#032F62","--shiki-dark":"#96D0FF"},children:'"Webhook created"'}),e.jsx(s.span,{style:{color:"#24292E","--shiki-dark":"#ADBAC7"},children:","})]}),`
`,e.jsxs(s.span,{className:"line",children:[e.jsx(s.span,{style:{color:"#005CC5","--shiki-dark":"#8DDB8C"},children:'  "hook_id"'}),e.jsx(s.span,{style:{color:"#24292E","--shiki-dark":"#ADBAC7"},children:": "}),e.jsx(s.span,{style:{color:"#032F62","--shiki-dark":"#96D0FF"},children:'"unique-hook-id"'})]}),`
`,e.jsx(s.span,{className:"line",children:e.jsx(s.span,{style:{color:"#24292E","--shiki-dark":"#ADBAC7"},children:"}"})})]})}),`
`,e.jsxs(s.ul,{children:[`
`,e.jsxs(s.li,{children:[e.jsx(s.strong,{children:"400 Bad Request"}),": Invalid query or webhook URL."]}),`
`]}),`
`,e.jsxs(s.h3,{id:"delete-webhookshook_id",children:["DELETE ",e.jsx(s.code,{children:"/webhooks/{hook_id}"}),e.jsx(s.a,{"aria-hidden":"true",tabIndex:"-1",href:"#delete-webhookshook_id",children:e.jsx(s.div,{"data-autolink-icon":!0})})]}),`
`,e.jsx(s.p,{children:"Removes a registered webhook by ID."}),`
`,e.jsx(s.strong,{children:"Parameters"}),`
`,e.jsxs(s.ul,{children:[`
`,e.jsxs(s.li,{children:[e.jsx(s.code,{children:"hook_id"})," (str): The unique ID of the webhook to delete."]}),`
`]}),`
`,e.jsx(s.strong,{children:"Response"}),`
`,e.jsxs(s.ul,{children:[`
`,e.jsxs(s.li,{children:[e.jsx(s.strong,{children:"200 OK"}),": Webhook deleted successfully."]}),`
`]}),`
`,e.jsx(s.pre,{className:"shiki shiki-themes github-light github-dark-dimmed",style:{backgroundColor:"#fff","--shiki-dark-bg":"#22272e",color:"#24292e","--shiki-dark":"#adbac7"},tabIndex:"0",children:e.jsxs(s.code,{children:[e.jsx(s.span,{className:"line",children:e.jsx(s.span,{style:{color:"#24292E","--shiki-dark":"#ADBAC7"},children:"{"})}),`
`,e.jsxs(s.span,{className:"line",children:[e.jsx(s.span,{style:{color:"#005CC5","--shiki-dark":"#8DDB8C"},children:'  "message"'}),e.jsx(s.span,{style:{color:"#24292E","--shiki-dark":"#ADBAC7"},children:": "}),e.jsx(s.span,{style:{color:"#032F62","--shiki-dark":"#96D0FF"},children:'"Webhook deleted"'}),e.jsx(s.span,{style:{color:"#24292E","--shiki-dark":"#ADBAC7"},children:","})]}),`
`,e.jsxs(s.span,{className:"line",children:[e.jsx(s.span,{style:{color:"#005CC5","--shiki-dark":"#8DDB8C"},children:'  "hook_id"'}),e.jsx(s.span,{style:{color:"#24292E","--shiki-dark":"#ADBAC7"},children:": "}),e.jsx(s.span,{style:{color:"#032F62","--shiki-dark":"#96D0FF"},children:'"unique-hook-id"'})]}),`
`,e.jsx(s.span,{className:"line",children:e.jsx(s.span,{style:{color:"#24292E","--shiki-dark":"#ADBAC7"},children:"}"})})]})}),`
`,e.jsxs(s.ul,{children:[`
`,e.jsxs(s.li,{children:[e.jsx(s.strong,{children:"404 Not Found"}),": Webhook not found."]}),`
`]}),`
`,e.jsxs(s.h3,{id:"get-webhooks",children:["GET ",e.jsx(s.code,{children:"/webhooks/"}),e.jsx(s.a,{"aria-hidden":"true",tabIndex:"-1",href:"#get-webhooks",children:e.jsx(s.div,{"data-autolink-icon":!0})})]}),`
`,e.jsx(s.p,{children:"Retrieves a list of all registered webhooks."}),`
`,e.jsx(s.strong,{children:"Response"}),`
`,e.jsxs(s.ul,{children:[`
`,e.jsxs(s.li,{children:[e.jsx(s.strong,{children:"200 OK"}),": List of registered webhooks."]}),`
`]}),`
`,e.jsx(s.pre,{className:"shiki shiki-themes github-light github-dark-dimmed",style:{backgroundColor:"#fff","--shiki-dark-bg":"#22272e",color:"#24292e","--shiki-dark":"#adbac7"},tabIndex:"0",children:e.jsxs(s.code,{children:[e.jsx(s.span,{className:"line",children:e.jsx(s.span,{style:{color:"#24292E","--shiki-dark":"#ADBAC7"},children:"{"})}),`
`,e.jsxs(s.span,{className:"line",children:[e.jsx(s.span,{style:{color:"#005CC5","--shiki-dark":"#8DDB8C"},children:'"hooks"'}),e.jsx(s.span,{style:{color:"#24292E","--shiki-dark":"#ADBAC7"},children:": ["})]}),`
`,e.jsx(s.span,{className:"line",children:e.jsx(s.span,{style:{color:"#24292E","--shiki-dark":"#ADBAC7"},children:"        {"})}),`
`,e.jsxs(s.span,{className:"line",children:[e.jsx(s.span,{style:{color:"#005CC5","--shiki-dark":"#8DDB8C"},children:'            "id"'}),e.jsx(s.span,{style:{color:"#24292E","--shiki-dark":"#ADBAC7"},children:": "}),e.jsx(s.span,{style:{color:"#032F62","--shiki-dark":"#96D0FF"},children:'"unique-hook-id"'}),e.jsx(s.span,{style:{color:"#24292E","--shiki-dark":"#ADBAC7"},children:","})]}),`
`,e.jsxs(s.span,{className:"line",children:[e.jsx(s.span,{style:{color:"#005CC5","--shiki-dark":"#8DDB8C"},children:'            "url"'}),e.jsx(s.span,{style:{color:"#24292E","--shiki-dark":"#ADBAC7"},children:": "}),e.jsx(s.span,{style:{color:"#032F62","--shiki-dark":"#96D0FF"},children:'"webhook-url"'}),e.jsx(s.span,{style:{color:"#24292E","--shiki-dark":"#ADBAC7"},children:","})]}),`
`,e.jsxs(s.span,{className:"line",children:[e.jsx(s.span,{style:{color:"#005CC5","--shiki-dark":"#8DDB8C"},children:'            "query"'}),e.jsx(s.span,{style:{color:"#24292E","--shiki-dark":"#ADBAC7"},children:": "}),e.jsx(s.span,{style:{color:"#032F62","--shiki-dark":"#96D0FF"},children:'"query-string"'})]}),`
`,e.jsx(s.span,{className:"line",children:e.jsx(s.span,{style:{color:"#24292E","--shiki-dark":"#ADBAC7"},children:"        },"})}),`
`,e.jsx(s.span,{className:"line",children:e.jsx(s.span,{style:{color:"#B31D28",fontStyle:"italic","--shiki-dark":"#FF938A","--shiki-dark-font-style":"italic"},children:"        ..."})}),`
`,e.jsx(s.span,{className:"line",children:e.jsx(s.span,{style:{color:"#24292E","--shiki-dark":"#ADBAC7"},children:"    ]"})}),`
`,e.jsx(s.span,{className:"line",children:e.jsx(s.span,{style:{color:"#24292E","--shiki-dark":"#ADBAC7"},children:"}"})})]})}),`
`,e.jsxs(s.h3,{id:"get-webhookshook_id",children:["GET ",e.jsx(s.code,{children:"/webhooks/{hook_id}"}),e.jsx(s.a,{"aria-hidden":"true",tabIndex:"-1",href:"#get-webhookshook_id",children:e.jsx(s.div,{"data-autolink-icon":!0})})]}),`
`,e.jsx(s.p,{children:"Retrieves a specific webhook by ID."}),`
`,e.jsx(s.strong,{children:"Parameters"}),`
`,e.jsxs(s.ul,{children:[`
`,e.jsxs(s.li,{children:[e.jsx(s.code,{children:"hook_id"})," (str): The unique ID of the webhook to retrieve."]}),`
`]}),`
`,e.jsx(s.strong,{children:"Response"}),`
`,e.jsxs(s.ul,{children:[`
`,e.jsxs(s.li,{children:[e.jsx(s.strong,{children:"200 OK"}),": Webhook details."]}),`
`]}),`
`,e.jsx(s.pre,{className:"shiki shiki-themes github-light github-dark-dimmed",style:{backgroundColor:"#fff","--shiki-dark-bg":"#22272e",color:"#24292e","--shiki-dark":"#adbac7"},tabIndex:"0",children:e.jsxs(s.code,{children:[e.jsx(s.span,{className:"line",children:e.jsx(s.span,{style:{color:"#24292E","--shiki-dark":"#ADBAC7"},children:"{"})}),`
`,e.jsxs(s.span,{className:"line",children:[e.jsx(s.span,{style:{color:"#005CC5","--shiki-dark":"#8DDB8C"},children:'  "hook"'}),e.jsx(s.span,{style:{color:"#24292E","--shiki-dark":"#ADBAC7"},children:": {"})]}),`
`,e.jsxs(s.span,{className:"line",children:[e.jsx(s.span,{style:{color:"#005CC5","--shiki-dark":"#8DDB8C"},children:'    "id"'}),e.jsx(s.span,{style:{color:"#24292E","--shiki-dark":"#ADBAC7"},children:": "}),e.jsx(s.span,{style:{color:"#032F62","--shiki-dark":"#96D0FF"},children:'"unique-hook-id"'}),e.jsx(s.span,{style:{color:"#24292E","--shiki-dark":"#ADBAC7"},children:","})]}),`
`,e.jsxs(s.span,{className:"line",children:[e.jsx(s.span,{style:{color:"#005CC5","--shiki-dark":"#8DDB8C"},children:'    "url"'}),e.jsx(s.span,{style:{color:"#24292E","--shiki-dark":"#ADBAC7"},children:": "}),e.jsx(s.span,{style:{color:"#032F62","--shiki-dark":"#96D0FF"},children:'"webhook-url"'}),e.jsx(s.span,{style:{color:"#24292E","--shiki-dark":"#ADBAC7"},children:","})]}),`
`,e.jsxs(s.span,{className:"line",children:[e.jsx(s.span,{style:{color:"#005CC5","--shiki-dark":"#8DDB8C"},children:'    "query"'}),e.jsx(s.span,{style:{color:"#24292E","--shiki-dark":"#ADBAC7"},children:": "}),e.jsx(s.span,{style:{color:"#032F62","--shiki-dark":"#96D0FF"},children:'"query-string"'})]}),`
`,e.jsx(s.span,{className:"line",children:e.jsx(s.span,{style:{color:"#24292E","--shiki-dark":"#ADBAC7"},children:"  }"})}),`
`,e.jsx(s.span,{className:"line",children:e.jsx(s.span,{style:{color:"#24292E","--shiki-dark":"#ADBAC7"},children:"}"})})]})}),`
`,e.jsxs(s.ul,{children:[`
`,e.jsxs(s.li,{children:[e.jsx(s.strong,{children:"404 Not Found"}),": Webhook not found."]}),`
`]}),`
`,e.jsxs(s.h2,{id:"event-query-format",children:["Event Query Format",e.jsx(s.a,{"aria-hidden":"true",tabIndex:"-1",href:"#event-query-format",children:e.jsx(s.div,{"data-autolink-icon":!0})})]}),`
`,e.jsx(s.p,{children:"Webhook queries are customizable to match specific blockchain event conditions, with the following supported parameters:"}),`
`,e.jsxs(s.ul,{children:[`
`,e.jsxs(s.li,{children:[e.jsx(s.strong,{children:"module"}),": Filters by blockchain module (e.g., ",e.jsx(s.code,{children:"module=staking"}),")."]}),`
`,e.jsxs(s.li,{children:[e.jsx(s.strong,{children:"type"}),": Filters by event type (e.g., ",e.jsx(s.code,{children:"type=transfer"}),")."]}),`
`,e.jsxs(s.li,{children:[e.jsx(s.strong,{children:"attribute"}),": Filters by event attribute (e.g., ",e.jsx(s.code,{children:"attribute=sender"}),")."]}),`
`,e.jsxs(s.li,{children:[e.jsx(s.strong,{children:"value"}),": Filters by specific event value (e.g., ",e.jsx(s.code,{children:"value=mantra1..."}),")."]}),`
`,e.jsxs(s.li,{children:[e.jsx(s.strong,{children:"address"}),": Filters by account address activity (e.g., ",e.jsx(s.code,{children:"address=mantra1..."}),")."]}),`
`,e.jsxs(s.li,{children:[e.jsx(s.strong,{children:"contract"}),": Filters by smart contract address activity (e.g., ",e.jsx(s.code,{children:"contract=mantra1..."}),")."]}),`
`]}),`
`,e.jsx(s.p,{children:"It is possible to make a combination of these. Events will be filtered in the order especified in the query."}),`
`,e.jsxs(s.p,{children:["Example Query: ",e.jsx(s.code,{children:'"module=bank&value=/cosmos.bank.v1beta1.MsgSend"'})]}),`
`,e.jsxs(s.h2,{id:"error-handling",children:["Error Handling",e.jsx(s.a,{"aria-hidden":"true",tabIndex:"-1",href:"#error-handling",children:e.jsx(s.div,{"data-autolink-icon":!0})})]}),`
`,e.jsx(s.p,{children:"All error responses include a detail field to explain the reason for the failure."}),`
`,e.jsxs(s.ul,{children:[`
`,e.jsxs(s.li,{children:[e.jsx(s.strong,{children:"400 Bad Request"}),": Returned for invalid queries or data inputs."]}),`
`,e.jsxs(s.li,{children:[e.jsx(s.strong,{children:"404 Not Found"}),": Returned if a requested webhook ID does not exist."]}),`
`,e.jsxs(s.li,{children:[e.jsx(s.strong,{children:"500 Internal Server Error"}),": Server encountered an error processing the request."]}),`
`]})]})}function a(n={}){const{wrapper:s}={...r(),...n.components};return s?e.jsx(s,{...n,children:e.jsx(i,{...n})}):i(n)}export{a as default,d as frontmatter};
