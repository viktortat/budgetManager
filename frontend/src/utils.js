import axios from 'axios'

export function getApiCategories(walletID, token) {
    const url = "/api/categories/" + "?wallet=" + walletID;
    return axios.get(url, { headers: { Authorization: 'JWT ' + token }});
};

export function getApiTransactions(walletID, token) {
    const url = "/api/transactions/" + "?wallet=" + walletID;
    return axios.get(url, { headers: { Authorization: 'JWT ' + token }});
};

export function getCurrentUser(token) {
    const url = "/api/auth/users/current/";
    return axios.get(url, { headers: { Authorization: 'JWT ' + token }});
};