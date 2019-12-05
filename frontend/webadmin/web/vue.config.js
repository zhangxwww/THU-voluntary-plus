module.exports = {
    devServer: {
        proxy: {
            '/api': {
              target: 'https://thuvplus.iterator-traits.com/api',
              changeOrigin: true,
              pathRewrite: {
                '^/api': ''
              }
            }
        }
    }
}