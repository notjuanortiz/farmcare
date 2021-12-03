import { BehaviorSubject } from 'rxjs';
import { handleResponse } from '../helpers/handle-response';

const API_URL = "http://localhost:8000/";

const currentUserSubject = new BehaviorSubject(JSON.parse(localStorage.getItem('token')));

export const AuthenticationService = {
  login,
  logout,
  currentUser: currentUserSubject.JSON,
  get currentUserValue() {
    return currentUserSubject.value;
  }
};

async function login(email, password) {
  console.log("Email: " + email);
  console.log("Password: " + password);
  const requestOptions = {
    method: 'POST',
    headers: {
      'Content-Type': 'application/json',
      'Accept': 'application/json',
    },
    body: JSON.stringify({ email, password })
  };

  const response = await fetch(API_URL + "api/token/", requestOptions)
  const json = await response.json();
  if (json.access) {
    localStorage.setItem('access-token', json.access);
    localStorage.setItem('refresh-token', json.refresh);
    currentUserSubject.next(json.access);
    console.log('Access token: ' + json.access);
    console.log('Refresh token: ' + json.refresh);
  }
}

async function logout() {
  // send logout request to destroy token
  const requestOptions = {
    method: "POST",
    headers: {
      "Content-Type": "application/json"
    },
    body: {}
  }

  await fetch(API_URL + "logout/", requestOptions);

  // clear current user context
  localStorage.removeItem('currentUser');
  currentUserSubject.next(null);

}