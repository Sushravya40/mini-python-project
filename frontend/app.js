const API_BASE = 'http://localhost:5000/api';

// DOM Elements
const checkStatusBtn = document.getElementById('check-status-btn');
const migrateBtn = document.getElementById('migrate-btn');
const oldPromptInput = document.getElementById('old-prompt');
const newPromptOutput = document.getElementById('new-prompt');
const messageEl = document.getElementById('migration-msg');

const statusElements = {
    dt: document.getElementById('dt-status'),
    v: document.getElementById('v-status'),
    ds: document.getElementById('ds-status'),
    fc: document.getElementById('fc-status')
};

// Check Backend Status (Demonstrates the fundamental concepts running)
checkStatusBtn.addEventListener('click', async () => {
    try {
        const response = await fetch(`${API_BASE}/status`);
        const data = await response.json();

        if (response.ok) {
            // Update UI to show successful check of Variables, Datatypes, etc.
            Object.values(statusElements).forEach(el => {
                el.textContent = 'Active & Running';
                el.classList.add('active');
            });
            checkStatusBtn.textContent = 'Backend Connected';
        }
    } catch (error) {
        console.error('Error connecting to backend:', error);
        alert('Could not connect to backend. Make sure it is running on port 5000.');
    }
});

// ChatGPT to Gemini Prompt Migration
migrateBtn.addEventListener('click', async () => {
    const prompt = oldPromptInput.value.trim();
    if (!prompt) return;

    migrateBtn.textContent = 'Migrating...';
    try {
        const response = await fetch(`${API_BASE}/migrate-prompt`, {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify({ prompt })
        });

        const data = await response.json();

        if (response.ok) {
            newPromptOutput.value = data.data.enhanced;
            messageEl.textContent = data.message;
            messageEl.style.color = 'var(--success)';
        } else {
            messageEl.textContent = data.error;
            messageEl.style.color = '#ef4444';
        }
    } catch (error) {
        messageEl.textContent = 'Failed to migrate prompt.';
        messageEl.style.color = '#ef4444';
    } finally {
        migrateBtn.textContent = 'Migrate';
    }
});
