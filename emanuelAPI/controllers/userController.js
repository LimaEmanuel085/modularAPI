const User = require('../models/user');
const bcrypt = require('bcrypt');

exports.viewUser = (req, res) => {
    res.send('User details');
}

exports.createUser = async (req, res) => {
    const { name, email, password, confirmPassword } = req.body;

    if (!name || !email || !password || !confirmPassword) {
        return res.status(400).json({
            message: 'Preencha todos os campos!'
        });
    }

    if (password !== confirmPassword) {
        return res.status(400).json({
            message: 'As senhas não conferem!'
        });
    }

    const userExists = await User.findOne({email: email});

    if (userExists) {
        return res.status(400).json({
            message: 'Usuário já existe!',
            message2: 'Tente fazer login!'
        });
    }

    const salt = await bcrypt.genSalt(10);
    const passwordHash = await bcrypt.hash(password, salt);

    const user = new User({
        name: name,
        email: email,
        password: passwordHash,
    });


    await user.save();
    res.status(201).json({
        message: 'Usuário criado com successo!',
        user: user
    });

}