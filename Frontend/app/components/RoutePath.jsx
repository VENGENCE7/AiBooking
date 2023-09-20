import React, { useEffect, useState } from 'react'

const RoutePath = (props) => {
const [showpath,setShowPath]=useState("")

useEffect(()=>{
    const places = [];
    const routes=props?.paths
    routes.forEach(route => {
        places.push(route.from);
    });
    places?.push(routes[routes.length - 1].to);
    const journey = places.join(' -> ');
    setShowPath(journey)
    },[])

  return (
    <div>{showpath}</div>
  )
}

export default RoutePath