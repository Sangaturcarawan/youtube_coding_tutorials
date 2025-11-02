const link = "https://www.youtube.com/watch?v=f8Z9JyB2EIE&t=581s"

import React from 'react';
import {
    View, 
    Text, 
    StyleSheet, 
    Flatlist, 
    Alert
} from 'react-native';

const App = () => {
    return (
        <View>
            <Text style={styles.text}>Hello World!</Text>
        </View>
    );
};

const styles = StyleSheet.create({
    text: {
        fontSize: 24,
        color: "blue",
        fontWeight: "bold",
    },
})

export default App;