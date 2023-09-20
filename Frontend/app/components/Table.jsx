import React from 'react'
import RoutePath from './RoutePath'
const Table = (props) => {
// book me a flight form blr to mel form this month 17th to 18th sorted by price

  return ( 
<div className="relative overflow-x-auto">
    <table className="w-full text-sm text-left text-gray-500 dark:text-gray-400">
        <thead className="text-xs text-gray-700 uppercase bg-gray-50 dark:bg-gray-700 dark:text-gray-400">
            <tr>
                <th scope="col" className="px-6 py-3">
                    Index
                </th>
                <th scope="col" className="px-6 py-3">
                    Price (AUD)
                </th>
                <th scope="col" className="px-6 py-3">
                    Seats
                </th>
                <th scope="col" className="px-6 py-3">
                    Stops
                </th>
                <th scope="col" className="px-6 py-3">
                    Route
                </th>
                <th scope="col" className="px-6 py-3">
                    Departure
                </th>
                <th scope="col" className="px-6 py-3">
                    Arrival
                </th>
            </tr>
        </thead>
        <tbody className='bg-red-200'>
            {props.data?.length>0 &&
            props.data?.map((d,i)=>{
            return(
                <tr className="border-b bg-gray-50 dark:bg-gray-800 dark:border-gray-700" key={i}>
                <th scope="row" className="px-6 py-4 font-medium text-gray-900 whitespace-nowrap dark:text-white">
                    {i+1}
                </th>
                <td className="px-6 py-4">
                    {d["price"]}
                </td>
                <td className="px-6 py-4">
                    {d?.availability === null ? 0 : d?.availability}
                </td>
                <td className="px-6 py-4">
                    {d.routes.length-1}
                </td>
                <td className="px-6 py-4">
                    <RoutePath paths={d.routes}/>
                </td>
                <td className="px-6 py-4">
                {d.departure}
                </td>
                <td className="px-6 py-4">
                    {d.arrival}
                </td>
            </tr>
            )}
        )
            }

        </tbody>
    </table>
</div>
  )
}

export default Table