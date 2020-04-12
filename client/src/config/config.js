const NODE_ENV = process.env.NODE_ENV || "development";

const defaults = {
    HOST: (process.env.VUE_APP_PYTHON_HOST && process.env.VUE_APP_PYTHON_PORT) ?`${process.env.VUE_APP_PYTHON_HOST}:${process.env.VUE_APP_PYTHON_PORT}` : "http://localhost:8080"
};

let config = {};
config.development = config.uat = config.production = defaults;

//Override config here...

let exportConfig;
if (typeof config[NODE_ENV] === 'undefined') {
    exportConfig = config.development;
} else {
    exportConfig = config[NODE_ENV];
}

export default exportConfig;