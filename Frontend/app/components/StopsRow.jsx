import React, { useEffect, useState } from "react";

const StopsRow = ({ showStops, origin }) => {
  const [stops, setStops] = useState([]);

  useEffect(() => {
    if (showStops?.length > 0) {
      const add = showStops.map((stop) => stop.destination.city_name);
      // Add origin at the beginning of the array
      setStops([origin, ...add]);
    }
  }, [showStops, origin]);

  return (
    <>
      {stops?.length > 0 &&
        stops?.map(
          (stop, index) =>
            // Check if it's not the last stop before rendering
            index < stops.length - 1 && (
              <div className="text-neutral-600 dark:text-neutral-50 flex justify-between items-center w-full">
                <span className="ml-2">{stop}</span>
                <span className="ml-2"> {"->"} </span>
                <span className="ml-2">{stops[index + 1]}</span>
              </div>
            )
        )}
    </>
  );
};

export default StopsRow;
