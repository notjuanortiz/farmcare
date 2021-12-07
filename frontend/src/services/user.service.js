import { authHeader } from "../helpers/auth-header";
import { handleResponse } from "../helpers/handle-response";

const API_URL = "http://localhost:8000";

const requestOptions = {
    method: 'GET',
    headers: authHeader()
};

export const UserService = {
    getPublicContent,
    getUserDashboard
}

// Requests homepage data (user does not have to be authorized to view public content)
function getPublicContent() {
    return fetch(API_URL, requestOptions)
        .then(handleResponse);
}

// Requests dashboard data (requires user to be authorized)
async function getUserDashboard() {
    return await fetch(API_URL + '/dashboard', requestOptions)
        .then(handleResponse);
}