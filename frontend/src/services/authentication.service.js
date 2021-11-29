import { BehaviorSubject } from 'rxjs';
import { handleResponse } from '../helpers/handle-response';

const API_URL = "http://localhost:8000/auth/";

const currentUserSubject = new BehaviorSubject(JSON.parse(localStorage.getItem('user')));

export const authenticationService = {
  login,
  logout,
  currentUser: currentUserSubject.asObservable(),
  get currentUser() {
    return currentUserSubject.value;
  }
};

function login(email, password) {
  console.log(email);
  console.log(password);
  const requestOptions = {
    method: "POST",
    headers: {
      "Content-Type": "application/json",
    },
    body: {
      "email": JSON.stringify(email),
      "password": JSON.stringify(password)
    }
  }
  return fetch(API_URL + "login/", requestOptions)
    .then(handleResponse)
    .then(user => {
      // set current user context
      localStorage.setItem('user', JSON.stringify(user));
      currentUserSubject.next(user);
    });
}

function logout() {
  // send logout request to destroy token
  const requestOptions = {
    method: "POST",
    headers: {
      "Content-Type": "application/json"
    },
    body: {}
  }

  fetch(API_URL + "logout/", requestOptions);

  // clear current user context
  localStorage.removeItem("user");
  currentUserSubject.next(null);

}