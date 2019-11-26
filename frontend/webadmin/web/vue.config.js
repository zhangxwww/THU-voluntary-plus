module.exports = {
    devServer: {
        proxy: {
            '/api': {
              target: 'https://thuvplus.iterator-traits.com',
              changeOrigin: true,
              pathRewrite: {
                '^/api': ''
            }
          }
        }
    }
}