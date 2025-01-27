import axios from 'axios';

const api = axios.create({
    baseURL: 'http://127.0.0.1:5005', // Backend portu 5005 olarak ayarlandı
});

export default api;
