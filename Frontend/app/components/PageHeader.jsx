import React from "react";
import { pressStart2P, instrumentSans } from "../styles/fonts";

const PageHeader = (props) => {
  return (
    <div>
      <div className={`${pressStart2P?.className} mb-10 text-6xl uppercase`}>
        {props?.heading}
      </div>
      <div className={`${instrumentSans?.className} mb-10`}>
        {props?.description}
      </div>
    </div>
  );
};

export default PageHeader;
