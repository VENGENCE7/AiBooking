import React from 'react'

const CardsRow = ({right,left}) => {
  return (
    <div className="text-neutral-600 dark:text-neutral-50 flex justify-between items-center w-full">
    <span className="ml-2">{right}</span>
    <span className="ml-2">{left}</span>
  </div>
  )
}

export default CardsRow;

