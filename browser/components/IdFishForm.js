import React from 'react'

export default class extends React.Component {
  constructor (props) {
    super(props)
    this.state = {}
    this.handleChange = this.handleChange.bind(this)
    this.sumbitFish = this.sumbitFish.bind(this)
  }

  sumbitFish (e) {
    e.preventDefault()
    this.props.handleFormSumbit(this.state)
  }

  handleChange (e) {
    this.setState({
      [e.target.name]: e.target.value
    })
  }

  render () {
    return (
      <form className='fish-form-container'>
        <div className='fish-form'>
          <label className='fish-form-label-size'>Size (cm)</label>
          <input className='fish-form-input-size' name='size' onChange={this.handleChange} />
        </div>
        <div className='clearfix' />
        <div className='fish-form'>
          <label className='fish-form-label-loc'>Location</label>
          <input className='fish-form-input-loc' name='location' onChange={this.handleChange} />
        </div>
        <div className='clearfix' />
        <button className='fish-form-btn' type='submit' onClick={this.sumbitFish}>ID FISH!</button>
      </form>
    )
  }
}
