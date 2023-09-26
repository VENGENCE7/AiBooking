import React from "react";

const Title = ({ emoji, headingText }) => {
  return (
    <div>
      <div>
        <h1 className="text-center mb-4 text-5xl">{emoji}</h1>
      </div>
      <div>
        <p className="text-center mb-8 text-2xl leading-tight text-primary">{headingText.toUpperCase()}</p>
      </div>
    </div>
  );
};

export default Title;
