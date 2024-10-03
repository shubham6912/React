import React from "react";
import ReactDOM from "react-dom/client";

//React Element => Object => HTMLElement(render)

const heading = React.createElement("h1", { id: "heading" }, "Namaste React");

console.log(heading);

//JSX
//HTML like syntax or XML like syntax

//React Element

const ele = <span> This is React Element Spam </span>;

// Wrap inside () for multiple lines
//console.log(jsxHeading);

//React Component
//Class based components OLD
//Functional components  NEW

//React funtional component

// A function that returns a piece of JSX code is called a functional component
// It starts with a capital Name
// All the below forms are perfectly fine syntax and diff ways of writing functional component
const fn = () => true;

const fn2 = () => {
  return true;
};

const fn3 = () => {
  true;
};

//Functions also can be used but industry practise is to use arrow
/*
const Title = function () {
  return <h1>Namaste React JS </h1>;
};
*/

const Title = () => <h1 className="head">Namaste React JS</h1>;

const title=(
  <h1 className="head" tabIndex="5">
    Namaste React Using JSX
  </h1>
)

const number = 10000;
//Component Composition
const HeadingComponent = () => (
  <div id="container">
    {title}
    <Title></Title>
    <Title />
    {Title()}
    <h1>This is coming for HeadingComponent</h1>
  </div>
);

const jsxHeading = (
  <h1 className="head" tabIndex="1">
    {ele}
    This is JSX heading
    <HeadingComponent />
  </h1>
);

const HeadingComponent2 = () => (
  <h1 className="heading2"> This is coming for HeadingComponent</h1>
);

//We will prefer the one with return statement

const root = ReactDOM.createRoot(document.getElementById("root"));

//Ideally a react element can be redenderd directly but for components a diff syntax

//React Element
//root.render(jsxHeading);

//React Component
root.render(<HeadingComponent />);
