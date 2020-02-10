const path = require("path");
const HtmlWebpackPlugin = require("html-webpack-plugin");

module.exports = {
    entry: "./src/index.tsx",
    devtool: "inline-source-map",
    module: {
        rules: [{
            test: /\.tsx?$/,
            use: "ts-loader",
            exclude: /node_modules/
        }]
    },
    resolve: {
        extensions: [".tsx", ".ts", ".js"]
    },
    plugins: [new HtmlWebpackPlugin()],
    stats: {
        // One of the two if I remember right
        entrypoints: false,
        children: false
    },
    output: {
        filename: "bundle.js",
        path: path.resolve(__dirname, "dist")
    }
};