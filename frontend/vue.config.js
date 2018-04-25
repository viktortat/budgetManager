module.exports = {
  lintOnSave: false,
  devServer: {
    proxy: {
      '/api': {
        target: 'http://127.0.0.1:8000/',
        ws: true,
        changeOrigin: true
      }
    }
  },
  pwa: {
    workboxPluginMode: 'GenerateSW',
    workboxOptions: {
        globPatterns: ['dist/*.{js,html,css}']
    }
  }
}