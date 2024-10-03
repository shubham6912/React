import React from "react";
import ReactDOM from "react-dom/client";

/*
const heading= React.createElement("h1",{
    id:'heading'
},"Hi From React");
*/

// Practise of initial classes 

const parent=React.createElement("div",{  id:"rootParent"},[
        React.createElement("div",{id:"child1"},[
            React.createElement("h1",
                {id:"heading1"},
                "First Heading"
            ),
            React.createElement("h1",
                {id:"heading2"},
                "Second Heading")
        ]),
        React.createElement("div",{id:"child2"},[
            React.createElement("h1",
                {id:"heading1"},
                "Third Heading"
            ),
            React.createElement("h1",
                {id:"heading2"},
                "Fourth Heading")
        ]),

    ]        
    )
    


const root = ReactDOM.createRoot(document.getElementById("root"));
root.render(parent);

