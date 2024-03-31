import axios from "axios";

const request = async (path) => {
  try {
    const response = await axios.get(path);
    return response;
  } catch (error) {
    console.error(error);
  }
};

const local = "http://127.0.0.1:5000";
const backendURL = local;

export const constructBackendURL = (endpoint) => {
  return `${backendURL}/${endpoint}`;
};

export const fetchAPIResponse = async (endpoint) => {
  return request(constructBackendURL(endpoint));
};

export const fetchAPI = async (endpoint) => {
  const response = await fetchAPIResponse(endpoint);
  return response?.data;
};
