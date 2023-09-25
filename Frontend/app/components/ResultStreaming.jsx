"use client";

import React from "react";

const ResultStreaming = ({ data }) => {
  return (
    <div className="bg-gray-100 p-6 rounded shadow mb-4">
      {/* If data is a string */}
      {typeof data === "string" && (
        <pre className="text-black-500 mb-4">{data}</pre>
      )}
      {/* If data is an object */}
      {data && <div className="text-black-500 mb-4">{data?.output}</div>}

      {/* If data has source documents (e.g. when querying from a VectorDBQAChain and returnSourceDocuments is true) */}
      {data &&
        data.sourceDocuments &&
        data.sourceDocuments.map((doc, index) => (
          <div key={index} className="bg-grey-100 p-1 rounded shadow mb-2">
            <div>
              Source {index}: {doc.pageContent}
            </div>
            <div className="text-gray-700">From: {doc.metadata.source}</div>
          </div>
        ))}
    </div>
  );
};

export default ResultStreaming;
