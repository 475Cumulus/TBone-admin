// webpack v4
const path = require('path');
const MiniCssExtractPlugin = require("mini-css-extract-plugin");
module.exports = {
    entry: { main: './static/js/index.js' },
    output: {
        path: path.resolve(__dirname, 'static/dist'),
        filename: 'index.js'
    },
    plugins: [
        new MiniCssExtractPlugin({})
    ],
    module: {
        rules: [
            {
                test: /\.js$/,
                exclude: /node_modules/,
                use: {
                    loader: "babel-loader"
                }
            },
            {
                test: /\.less$/,
                use:[
                    {
                        loader: MiniCssExtractPlugin.loader
                    },
                    'style-loader',
                    'css-loader',
                    'less-loader'
                ]
            }
        ]
    }
};