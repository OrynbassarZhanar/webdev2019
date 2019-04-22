export interface TaskList{
    id:number;
    name:string;
}
export interface Task{
  task_list: any;
    id: number;
    name:string;
    created_at: Date;
    due_on: Date;
    status: string;
}