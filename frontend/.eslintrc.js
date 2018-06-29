module.exports = {
  root: true,
  env: {
    node: true
  },
  extends: [
    "plugin:vue/strongly-recommended",
    "plugin:prettier/recommended"
  ],
  rules: {
    'no-console': 'off',
    'vue/require-default-prop': 'off'
  },
  parserOptions: {
    parser: 'babel-eslint',
    ecmaVersion: 2017
  }
}