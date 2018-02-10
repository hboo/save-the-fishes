import React from 'react'
import LearnMore from './LearnMore'

export default (props) =>
  <div className='species-container'>
    <p className='species-text'>{props.species}</p>
    <LearnMore />
  </div>
