"use strict";

const balanceTransfer = require("./lib/balanceTransfer");
const autorium = require("./lib/autorium");

module.exports.BalanceTransfer = balanceTransfer;
module.exports.Autorium = autorium;
module.exports.contracts = [balanceTransfer, autorium];
