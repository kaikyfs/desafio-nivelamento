import axios from "axios";

const baseURL = 'http://127.0.0.1:5000'

async function getOperadoras() {
    try {
        const response = await axios.get(`${baseURL}/api/operadora`);
        return response.data;
    } catch (error) {
        console.error("Error fetching operadoras:", error);
        throw error;
    }
}

async function getOperadora(nome) {
    try {
        const response = await axios.get(`${baseURL}/api/operadora/${nome}`);
        return response.data;
    } catch (error) {
        console.error("Error fetching operadora:", error);
        throw error;
    }
}

export { getOperadora, getOperadoras };