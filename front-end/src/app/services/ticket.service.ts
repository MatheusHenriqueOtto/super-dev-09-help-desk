import { HttpClient } from '@angular/common/http';
import { inject, Service } from '@angular/core';
import { Observable } from 'rxjs';
import { TicketResposta } from '../models/tickets.model';

@Service()
export class TicketService {
    /*HttpClient é o cliente que utilizarmos no angular para fazer requests */
    private http = inject(HttpClient);

// URL do back-end por enquanto está fixo, depois
// utilizaremos environment para ser dinâmico
    private baseUrl = `http://localhost:8000/tickets`


    // função que será responsável por comunicar com o back
    // para obter a lista de tickets
    listar(): Observable<TicketResposta[]>{
        // faz a requisição  para /tickets no back-end
        return this.http.get    <TicketResposta[]>(this.baseUrl)
    }
}
