import React from "react";
import Image from "next/image";
import CardsRow from "./CardsRow";
import StopsRow from "./StopsRow";

const FlightCards = ({ offers, handleFlightClick }) => {
  return (
    <div className="grid grid-cols-1 sm:grid-cols-2 md:grid-cols-4 gap-4 w-full">
      {offers?.length > 0 &&
        offers?.slice(0, 4).map((item, index) => (
          <div
            key={index}
            className="block max-w-[18rem] rounded-lg border border-info bg-white-700 shadow-[0_2px_15px_-3px_rgba(0,0,0,0.07),0_10px_20px_-2px_rgba(0,0,0,0.04)] dark:border-info-300 dark:bg-neutral-600 mb-3 shadow-xl"
          >
            <div className="border-b-2 border-[#0000002d] px-6 py-3 text-neutral-600 dark:text-neutral-50 flex justify-between items-center w-full">
              <span className="ml-2">{item.owner.name}</span>
              <div className="flex items-center">
                <Image
                  src={item?.owner?.logo_symbol_url}
                  alt={item.owner}
                  className="rounded-lg shadow-purple-500/40 shadow-lg"
                  priority
                  unoptimized
                  width={32}
                  height={32}
                />
              </div>
            </div>

            <div className="p-6">
              {/* <p className="text-base text-info dark:text-info-300">
                {item.owner.name}
              </p> */}
              <h5 className="mb-2 text-xl font-medium leading-tight text-info dark:text-info-300 text-center">
                {item.total_amount + " " + item.tax_currency}
              </h5>
              <CardsRow
                right={"Stops"}
                left={item?.slices[0]?.segments?.length}
              />
              <StopsRow showStops={item?.slices[0]?.segments} origin={item?.slices[0]?.origin.city_name}/>
              <div className="flex">
                <button
                  onClick={() => {
                    handleFlightClick(index + 1, item.total_amount);
                  }}
                  className={`py-3 m-4 px-6 bg-white shadow-lg text-gray-900 font-semibold rounded-full hover:shadow-xl transition-colors duration-200 w-full`}
                >
                  Book Now
                </button>
              </div>
            </div>
          </div>
        ))}
    </div>
  );
};

export default FlightCards;
