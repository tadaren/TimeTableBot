const vm = new Vue({
    el: '#timetable',
    data: {
        timetable: {}
    },
    mounted(){
        let today = new Date();
        let todayString = today.toISOString().substr(0, 10);
        this.getTimetable(todayString);
    },
    methods: {
        getTimetable(date) {
            axios.get('/api/timetable/get?date='+date).then(response => {
                console.log(response);
                this.timetable = response.data;
            }).catch(
            )
        }
    }
})
