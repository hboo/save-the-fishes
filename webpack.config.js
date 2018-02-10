'use strict'

module.exports = {
    entry: './browser/index.js',
    output: {
        filename: './static/bundle.js'
    },
    module: {
        rules: [{
            test: /\.js$/,
            loader: 'babel-loader',
            options: {
                presets: ['es2015', 'react']
            }
        }]
    }
}
