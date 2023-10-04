import React from "react";

const TwoColumnLayout = ({ rightChildren }) => (
  <div className="flex flex-col justify-between  md:flex-row md:justify-between">
    <div className="md:w-5/5 w-full">{rightChildren}</div>
  </div>
);

export default TwoColumnLayout;
