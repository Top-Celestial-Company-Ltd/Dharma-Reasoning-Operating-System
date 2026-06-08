const { Worker } = require('worker_threads');
const fs = require('fs');

const promptFile = process.argv[2];
const model = process.argv[3];
const cliPath = 'C:/Users/Jimmy/AppData/Roaming/npm/node_modules/@google/gemini-cli/bundle/gemini.js';

const prompt = fs.readFileSync(promptFile, 'utf8');

// Spawn the gemini.js in an in-memory worker thread to bypass Windows 8,191 CMD limits
new Worker(cliPath, { 
    argv: ['--skip-trust', '--model', model, '-p', prompt],
    env: Object.assign({}, process.env, { GEMINI_CLI_NO_RELAUNCH: '1' })
});
