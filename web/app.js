const vm = new Vue({
    el: '#timetable',
    data: {
        date: '',
        timetable: {}
    },
    mounted(){
        let today = new Date();
        let todayString = today.toISOString().substr(0, 10);
        this.date = todayString;
    },
    watch: {
        date: function(newDate){
            this.getTimetable(newDate);
        }
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
