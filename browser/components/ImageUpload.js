import React from 'react'
import FileDrop from 'react-file-drop'
import request from 'superagent'

const CLOUDINARY_UPLOAD_PRESET = 'fq1rxfrr'
const CLOUDINARY_UPLOAD_URL = 'https://api.cloudinary.com/v1_1/dpaa0igrr/upload'

export default class extends React.Component {
  constructor (props) {
    super(props)
    this.state = {
      uploadedFileCloudinaryUrl: ''
    }
    this.onImageDrop = this.onImageDrop.bind(this)
    this.handleImageUpload = this.handleImageUpload.bind(this)
  }

  onImageDrop (files) {
    console.log('FILES IN onImageDrop', files)
    this.setState({
      uploadedFile: files[0]
    })
    this.handleImageUpload(files[0])
  }

  handleImageUpload (file) {
    let upload = request.post(CLOUDINARY_UPLOAD_URL)
                        .field('upload_preset', CLOUDINARY_UPLOAD_PRESET)
                        .field('file', file)

    upload.end((err, response) => {
      if (err) {
        console.log(err)
      }

      if (response.body.secure_url !== '') {
        this.setState({
          uploadedFileCloudinaryUrl: response.body.secure_url
        }, () => console.log('STATE', this.state))
      }
    })
  }

  render () {
    return (
      <div>
        {
          this.state.uploadedFileCloudinaryUrl.length
            ? <img src={this.state.uploadedFileCloudinaryUrl} />
            : <FileDrop className='drop-fish-img' frame={document} onDrop={this.onImageDrop}>
                  Drop your fish image here
              </FileDrop>
        }
      </div>
    )
  }
}
