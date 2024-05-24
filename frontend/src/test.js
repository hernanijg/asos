import axios from 'axios';

const API_URL = 'http://localhost:8000/api/testurl/';

export const getTestModels = () => {
    return axios.get(API_URL);
};

export const createTestModel = (data) => {
    return axios.post(API_URL, data);
};

export const updateTestModel = (id, data) => {
    return axios.put(`${API_URL}${id}/`, data);
};

export const deleteTestModel = (id) => {
    return axios.delete(`${API_URL}${id}/`);
};
