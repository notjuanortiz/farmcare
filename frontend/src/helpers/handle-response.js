import { AuthenticationService } from "../services/authentication.service";

export function handleResponse(response) {
    console.log(response.json());
    return response.text().then(text => {
        const data = text && JSON.parse(text);

        if (!response.ok) {
            if ([401, 403].indexOf(response.status) !== -1) {
                AuthenticationService.logout();
                this.location.reload(true);
            }

            const error = (data && data.message) || response.statusText;
            return Promise.reject(error);
        }
    })
}