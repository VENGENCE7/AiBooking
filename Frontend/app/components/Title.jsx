import React from "react";

const Title = ({ emoji, headingText }) => {
  return (
    <div>
      <div>
        <h1 className="text-center mb-4">{emoji}</h1>
      </div>
      <div>
        <p className="text-center mb-8">{headingText.toUpperCase()}</p>
      </div>
    </div>
  );
};

export default Title;
