import Vue from "vue";

Vue.filter(
  "formatCurrency",
  value =>
    `${value
      .toString()
      .replace(/\B(?=(\d{3})+(?!\d))/g, " ")
      .replace(".", ",")} Kč`
);

Vue.filter("shortenString", (value, lng) => {
  if (value) {
    if (value.length > lng) {
      return `${value.substring(0, lng).trim()}...`;
    }

    return value;
  }

  return "--";
});

Vue.filter("appendMinusSign", (value, type) => {
  if (type === "expense") {
    return `- ${value}`;
  }

  return value;
});

Vue.filter("formatNumber", value => {
  const num = parseFloat(value);

  return num.toFixed(2);
});

Vue.filter("formatPercents", value => `${value * 100} %`);
