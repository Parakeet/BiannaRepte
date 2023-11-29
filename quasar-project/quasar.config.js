// quasar.conf.js

module.exports = function (/* ctx */) {
  return {
    // Otras configuraciones de Quasar

    devServer: {
      proxy: {
        '/vendes': {
          target: 'http://127.0.0.1:8000',
          changeOrigin: true,
          pathRewrite: {
            '^/vendes': '/vendes',
          },
        },
      },
    },

    // Otras configuraciones de Quasar
  };
};

