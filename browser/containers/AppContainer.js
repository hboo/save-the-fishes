import React from 'react'

import Header from '../components/Header.js'
import ImageUpload from '../components/ImageUpload.js'

export default class extends React.Component {
  constructor (props) {
    super(props)
    this.state = {}
  }

  render () {
    return (
      <div>
        <Header />
        <ImageUpload />
      </div>
    )
  }
}
