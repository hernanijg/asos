import React, { useState, useEffect } from 'react';
import { getTestModels, createTestModel, updateTestModel, deleteTestModel } from './test';

export const TestModelComponent = () => {
    const [testModels, setTestModels] = useState([]);
    const [newTestModel, setNewTestModel] = useState('');

    useEffect(() => {
        fetchTestModels();
    }, []);

    const fetchTestModels = async () => {
        try {
            const response = await getTestModels();
            setTestModels(response.data);
        } catch (error) {
            console.error('Error fetching test models:', error);
        }
    };

    const handleCreate = async () => {
        try {
            const response = await createTestModel({ name: newTestModel });
            setTestModels([...testModels, response.data]);
            setNewTestModel('');
        } catch (error) {
            console.error('Error creating test model:', error);
        }
    };

    const handleUpdate = async (id) => {
        const updatedName = prompt('Enter new name:');
        if (updatedName) {
            try {
                const response = await updateTestModel(id, { name: updatedName });
                setTestModels(testModels.map((tm) => (tm.id === id ? response.data : tm)));
            } catch (error) {
                console.error('Error updating test model:', error);
            }
        }
    };

    const handleDelete = async (id) => {
        try {
            await deleteTestModel(id);
            setTestModels(testModels.filter((tm) => tm.id !== id));
        } catch (error) {
            console.error('Error deleting test model:', error);
        }
    };

    return (
        <div>
            <h1>Test Models</h1>
            <ul>
                {testModels.map((tm) => (
                    <li key={tm.id}>
                        {tm.name} 
                        <button onClick={() => handleUpdate(tm.id)}>Update</button>
                        <button onClick={() => handleDelete(tm.id)}>Delete</button>
                    </li>
                ))}
            </ul>
            <input
                type="text"
                value={newTestModel}
                onChange={(e) => setNewTestModel(e.target.value)}
                placeholder="New Test Model"
            />
            <button onClick={handleCreate}>Create</button>
        </div>
    );
};

