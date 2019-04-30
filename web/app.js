const vm = new Vue({
    el: '#timetable',
    data: {
        date: '',
        timetable: {},
        tasks: [],
        deadline: '',
        subject: '',
        detail: '',
        tags: '',
    },
    mounted(){
        let today = new Date();
        let todayString = today.toISOString().substr(0, 10);
        this.date = todayString;
        this.deadline = todayString;
    },
    watch: {
        date: function(newDate){
            this.getTimetable(newDate);
            this.getTasks(newDate);
        }
    },
    methods: {
        getTimetable(date) {
            axios.get('/api/timetable/get?date='+date).then(response => {
                console.log(response);
                this.timetable = response.data;
            }).catch(error => {
                console.error(error);
            })
        },
        getTasks(date) {
            let param = {
                first_day: date,
                last_day: date,
            };
            axios.get('/api/task/get', param).then(response => {
                console.log(response);
                this.tasks = response.data.response;
            }).catch(error => {
                console.error(error);
            })
        },
        addTask(){
            let param = {
                'deadline': this.deadline,
                'subject': this.subject,
                'detail': this.detail,
                'tags': []
            };
            axios.post('/api/task/add', param);
        },
    }
})
